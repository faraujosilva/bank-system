package operations

import "bank-system/pkg/entities"

type IAccountOperation interface {
	Debit(amount float32) (string, error)
	Credit(amount float32) (string, error)
}

type IOperationMethod interface {
	DoTransaction(sender, recipient entities.IPerson, amount float32) (string, error)
	validateTransaction(sender, recipient entities.IPerson, amount float32) bool
}
