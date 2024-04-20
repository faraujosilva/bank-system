package operations

import (
	"bank-system/pkg/entities"
	"fmt"
	"log"
)

type TED struct{}

func (t *TED) DoTransaction(sender, recipient entities.IPerson, amount float32) (string, error) {
	log.Println("Starting TED transaction")
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
		return "TED transaction completed", nil
	}
	return "Error", fmt.Errorf("Error")
}

func (t *TED) validateTransaction(sender, recipient entities.IPerson, amount float32) bool {
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
