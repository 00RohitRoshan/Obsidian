package models

import "gorm.io/gorm"

type Tag struct {
	gorm.Model
	Name  string `json:"name" gorm:"unique"`
	Posts []Post `gorm:"many2many:post_tags;"` // Many-to-Many
}
