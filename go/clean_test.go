package tests

import (
	entity "bank-system/pkg/entities"
	"bank-system/pkg/operations"
	"bank-system/pkg/services"
	"testing"

	"github.com/stretchr/testify/assert"
)

var person1, _ = entity.NewPerson("Fernando", "19/05/1997", "Brazil", "43212343123")
var account1, _ = entity.NewAccount("123", "current", 1000.0)

var person2, _ = entity.NewPerson("Miro", "19/05/1995", "Brazil", "12312343123")
var account2, _ = entity.NewAccount("321", "current", 1000.0)

func TestPerson(t *testing.T) {
	assert.Equal(t, "Fernando", person1.Name)
	assert.Equal(t, "Brazil", person1.Country)

}
func TestGetAge(t *testing.T) {
	assert.Equal(t, 27, person1.GetAge())
}

func TestPersonAccount(t *testing.T) {
	person1.AddAccount(account1)
	account1.SetOwner(person1.Identity)
	person2.AddAccount(account2)
	account2.SetOwner(person2.Identity)
	assert.Equal(t, "43212343123", account1.GetOwner())
	assert.Equal(t, "123", person1.ClientAccount.AccountNumber())
	assert.Equal(t, "12312343123", account2.GetOwner())
	assert.Equal(t, "321", person2.ClientAccount.AccountNumber())
}

func TestTED(t *testing.T) {
	ted := &operations.TED{}

	person1CurrentOperation := &services.CurrentAccountOperation{
		Sender:    person1,
		Recipient: person2,
		Method:    ted,
	}

	person1Operation := services.AccountService{
		Person:    person1,
		Operation: person1CurrentOperation,
	}

	person1Operation.UpdateBalance(-300)
	assert.Equal(t, float32(700), person1.ClientAccount.GetBalance())
	assert.Equal(t, float32(1300), person2.ClientAccount.GetBalance())
}

func TestPIX(t *testing.T) {
	person1.ClientAccount.UpdateBalance(300) // Restore original value for make sense test
	person2.ClientAccount.UpdateBalance(-300)
	pix := &operations.PIX{}

	person1CurrentOperation := &services.CurrentAccountOperation{
		Sender:    person1,
		Recipient: person2,
		Method:    pix,
	}

	person1Operation := services.AccountService{
		Person:    person1,
		Operation: person1CurrentOperation,
	}

	person1Operation.UpdateBalance(-300)
	assert.Equal(t, float32(700), person1.ClientAccount.GetBalance())
	assert.Equal(t, float32(1300), person2.ClientAccount.GetBalance())
}
