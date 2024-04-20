package entities

import (
	"fmt"
)

type Account struct {
	Number        string
	AccountType   string
	Balance       float32
	Owner         string
	SpecialCredit float32
}

type IAccount interface {
	AccountNumber() string
	GetOwner() string
	Type() string
	GetSpecialCredit() float32
	SetSpecialCredit(limit float32) error
	GetBalance() float32
	SetOwner(identity string) error
	UpdateBalance(amount float32)
	haveOwner() bool
}

func NewAccount(number, accountType string, balance float32) (*Account, error) {
	if number == "" || accountType == "" {
		return &Account{}, fmt.Errorf("You need to provide number and account type")
	}
	return &Account{
		Number:        number,
		AccountType:   accountType,
		Balance:       balance,
		SpecialCredit: 0.0,
	}, nil
}

func (a *Account) GetOwner() string {
	return a.Owner
}

func (a *Account) GetSpecialCredit() float32 {
	return a.SpecialCredit
}

func (a *Account) AccountNumber() string {
	return a.Number
}

func (a *Account) Type() string {
	return a.AccountType
}

func (a *Account) SetSpecialCredit(limit float32) error {
	if limit == 0 {
		return fmt.Errorf("You provided a invalid new limit")
	}
	a.SpecialCredit = +limit
	return nil
}

func (a *Account) GetBalance() float32 {
	if a.haveOwner() {
		return a.Balance
	}
	return 0.0
}

func (a *Account) SetOwner(identity string) error {
	if identity == "" {
		return fmt.Errorf("You provided a empty owner")
	}
	a.Owner = identity
	return nil
}

func (a *Account) UpdateBalance(amount float32) {
	if a.haveOwner() {
		if a.Balance < float32(0) {
			if amount > float32(0) {
				a.Balance += amount
			} else {
				a.Balance -= amount
			}
		} else if a.Balance == float32(0) {
			if amount > float32(0) {
				a.Balance += (amount * -1)
			} else {
				a.Balance += amount
			}
		} else {
			a.Balance += amount
		}
	}
}

func (a *Account) haveOwner() bool {
	if a.Owner != "" {
		return true
	} else {
		return false
	}
}
