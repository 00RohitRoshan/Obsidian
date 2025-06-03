package controllers

import (
	config "build/Gorm/Config"
	models "build/Gorm/Models"
	"fmt"
)

func CreateUser(name string, email string) {
	user := models.User{Name: name, Email: email}
	result := config.DB.Create(&user)
	if result.Error != nil {
		fmt.Println("Error creating user:", result.Error)
		return
	}
	fmt.Println("User created:", user)
}

func ListUsers() {
	var users []models.User
	config.DB.Find(&users)
	for _, u := range users {
		fmt.Printf("ID: %d, Name: %s, Email: %s\n", u.ID, u.Name, u.Email)
	}
}

func UpdateUserEmail(id uint, newEmail string) {
	var user models.User
	config.DB.First(&user, id)
	user.Email = newEmail
	config.DB.Save(&user)
	fmt.Println("User updated:", user)
}

func DeleteUser(id uint) {
	config.DB.Delete(&models.User{}, id)
	fmt.Println("User deleted with ID:", id)
}
