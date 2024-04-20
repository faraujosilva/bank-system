package services

import (
	"bank-system/pkg/entities"
	"bank-system/pkg/operations"
	"fmt"
	"log"
)

type IAccountService interface {
	UpdateBalance(amount float32) (string, error)
}

type AccountService struct {
	Person    entities.IPerson
	Operation operations.IAccountOperation
}

func (a *AccountService) UpdateBalance(amount float32) (string, error) {
	clientAccount, err := a.Person.GetAccount()
	if err != nil {
		return "", err
	}
	clientBalance := clientAccount.GetBalance()
	clientSpecialBalance := clientAccount.GetSpecialCredit()

	if amount > 0 {
		log.Println("Doing Credit transaction 1")
		a.Operation.Credit(amount)
		return "Success credit", nil
	}

	if clientBalance < 0 {
		if (amount*-1) > ((clientBalance*-1)+clientSpecialBalance) || clientBalance+(clientSpecialBalance*-1) > clientBalance+amount {
			return "No Enough Limit", fmt.Errorf("No Enough Limit")
		}
		a.Operation.Debit(amount)
		log.Println("Doing Debit transaction 1")
		return "Success debit", nil
	}

	if ((clientBalance + clientSpecialBalance) - (amount * -1)) < 0 {
		return "No Enough Limit", fmt.Errorf("No Enough Limit")

	}
	log.Println("Doing Debit transaction 2")
	a.Operation.Debit(amount)
	return "Success debit", nil

}
