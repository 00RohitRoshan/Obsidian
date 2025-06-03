package gormPractice

import (
	config "build/Gorm/Config"
	controllers "build/Gorm/Controllers"
	models "build/Gorm/Models"

	"github.com/go-faker/faker/v4"
)

// Entry point to the gorm_practice
func Gorm() {
	config.ConnectDB()
	config.DB.AutoMigrate(&models.User{})

	controllers.CreateUser("Alice", "alice@example.com")
	controllers.CreateUser("Bob", "bob@example.com")

	controllers.ListUsers()

	controllers.UpdateUserEmail(1, "alice@newdomain.com")

	controllers.ListUsers()

	controllers.DeleteUser(2)

	controllers.ListUsers()
}

func Relation() {
	config.ConnectDB()

	// AutoMigrate all models
	config.DB.AutoMigrate(&models.User{}, &models.Post{}, &models.Tag{})

	// Create sample data
	user := models.User{Name: faker.Name(), Email: faker.Email()}
	config.DB.Create(&user)

	post1 := models.Post{Title: "GORM Relationships", Body: "Let's understand relationships.", UserID: user.ID}
	post2 := models.Post{Title: "Second Post", Body: "More content here.", UserID: user.ID}

	config.DB.Create(&post1)
	config.DB.Create(&post2)

	tag1 := models.Tag{Name: "golang"}
	tag2 := models.Tag{Name: "gorm"}
	config.DB.Create(&tag1)
	config.DB.Create(&tag2)

	// Associate tags with posts (Many-to-Many)
	config.DB.Model(&post1).Association("Tags").Append(&tag1, &tag2)
	config.DB.Model(&post2).Association("Tags").Append(&tag2)
}
