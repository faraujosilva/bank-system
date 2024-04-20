package entities

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

type Person struct {
	Name          string
	BornDate      string
	Country       string
	Identity      string
	ClientAccount IAccount
}

type IPerson interface {
	GetName() string
	GetAge() int
	GetCountry() string
	GetIdentity() string
	GetAccount() (IAccount, error)
	AddAccount(account IAccount) error
	RemoveAccount(account IAccount) error
}

func NewPerson(name, borndate, country, identity string) (*Person, error) {
	if name == "" || borndate == "" || country == "" || identity == "" {
		return &Person{}, fmt.Errorf("You provied some values nil, retry please")
	}
	if err := validateBornDate(borndate); err != nil {
		return &Person{}, err
	}

	return &Person{
		Name:     name,
		BornDate: borndate,
		Country:  country,
		Identity: identity,
	}, nil

}

func (p *Person) GetName() string {
	return p.Name
}

func (p *Person) GetAge() int {
	currentYear := time.Now().Year()
	bornYearStr := strings.Split(p.BornDate, "/")[2]

	bornyear, err := strconv.Atoi(bornYearStr)
	if err != nil {
		return 18
	}

	return currentYear - bornyear
}

func (p *Person) GetCountry() string {
	return p.Country
}

func (p *Person) GetIdentity() string {
	return p.Identity
}

func (p *Person) GetAccount() (IAccount, error) {
	if p.ClientAccount.AccountNumber() != "" {
		return p.ClientAccount, nil
	}
	return nil, fmt.Errorf("Client do not have an account")
}

func (p *Person) AddAccount(account IAccount) error {
	if account == nil {
		return fmt.Errorf("Account type or number is invalid")
	}
	p.ClientAccount = account
	return nil
}

func (p *Person) RemoveAccount(account IAccount) error {
	if p.ClientAccount.Type() == "" || p.ClientAccount.AccountNumber() == "" {
		return fmt.Errorf("Client do not have any account to remove")
	}
	if p.ClientAccount.AccountNumber() != account.AccountNumber() {
		return fmt.Errorf("This account do not have ownership by %s", p.Name)

	}
	p.ClientAccount = account
	return nil
}

func validateBornDate(date string) error {
	if !strings.Contains(date, "/") {
		return fmt.Errorf("Date must be DAY/MONTH/YEAR")
	}
	yearStr := strings.Split(date, "/")[2]
	month := strings.Split(date, "/")[1]
	dayStr := strings.Split(date, "/")[0]
	day, err := strconv.Atoi(dayStr)
	if err != nil {
		return err
	}

	if day < 1 || day > 31 {
		return fmt.Errorf("Day must be at 1 and 31, you provide: %d", day)
	}

	if len(month) < 1 || len(month) > 2 {
		return fmt.Errorf("Month must have at least 1 and max 2 digit, you provide: %d", day)
	}

	monthInt, err := strconv.Atoi(month)
	if err != nil {
		return err
	}

	if monthInt < 1 || monthInt > 12 {
		return fmt.Errorf("Month must be at 1 and 12, you provide: %d", monthInt)
	}

	year, err := strconv.Atoi(yearStr)
	if err != nil {
		return err
	}

	if len(yearStr) < 4 {
		return fmt.Errorf("Year must have at least 4 digits, you provide: %d", year)
	}

	now := time.Now()
	currentYear := now.Year()

	if year > currentYear {
		return fmt.Errorf("The max year can you provide is %d", currentYear)
	}

	if currentYear-year < 18 {
		return fmt.Errorf("'You need to be older than 18 years")
	}

	return nil
}
