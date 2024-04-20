package operations

import (
	"bank-system/pkg/entities"
	"fmt"
	"log"
)

type PIX struct{}

func (t *PIX) DoTransaction(sender, recipient entities.IPerson, amount float32) (string, error) {
	log.Println("Starting PIX transaction")
	if t.validateTransaction(sender, recipient, amount) {
		senderAcc, err := sender.GetAccount()
		if err != nil {
			return "Cannot do transaction", fmt.Errorf("cannot do transaction")
		}
		senderAcc.UpdateBalance(amount)
		recipAcc, err := recipient.GetAccount()
		if err != nil {
			return "Cannot do transaction", fmt.Errorf("cannot do transaction")
		}
		recipAcc.UpdateBalance((amount * -1))
		return "PIX transaction completed", nil
	}
	return "Error", fmt.Errorf("Error")
}

func (t *PIX) validateTransaction(sender, recipient entities.IPerson, amount float32) bool {
	senderacc, err := sender.GetAccount()
	if err != nil {
		return false
	}
	recipientAcc, err := recipient.GetAccount()
	if err != nil {
		return false
	}
	return senderacc.GetOwner() == sender.GetIdentity() && recipientAcc.GetOwner() == recipient.GetIdentity() && amount != 0
}
