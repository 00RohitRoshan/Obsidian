package models

import "gorm.io/gorm"

type Post struct {
	gorm.Model
	Title  string `json:"title"`
	Body   string `json:"body"`
	UserID uint   // Foreign key for User

	Tags []Tag `gorm:"many2many:post_tags;"` // Many-to-Many
}
