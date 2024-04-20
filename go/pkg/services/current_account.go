package services

import (
	"bank-system/pkg/entities"
	"bank-system/pkg/operations"
)

type CurrentAccountOperation struct {
	Sender    entities.IPerson
	Recipient entities.IPerson
	Method    operations.IOperationMethod
}

func (caop *CurrentAccountOperation) Debit(amount float32) (string, error) {
	return caop.Method.DoTransaction(caop.Sender, caop.Recipient, amount)
}

func (caop *CurrentAccountOperation) Credit(amount float32) (string, error) {
	return caop.Method.DoTransaction(caop.Sender, caop.Recipient, amount)
}
