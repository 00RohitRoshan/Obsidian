package main

import (
    "github.com/gofiber/fiber/v2"
)

type Book struct {
    ID     string `json:"id"`
    Title  string `json:"title"`
    Author string `json:"author"`
}

var books = []Book{
    {ID: "1", Title: "1984", Author: "George Orwell"},
    {ID: "2", Title: "The Go Programming Language", Author: "Alan Donovan"},
}

func main() {
    app := fiber.New()

    app.Get("/books", getBooks)
    app.Get("/books/:id", getBookByID)
    app.Post("/books", createBook)
    app.Put("/books/:id", updateBook)
    app.Delete("/books/:id", deleteBook)

    app.Listen(":3000")
}

func getBooks(c *fiber.Ctx) error {
    return c.JSON(books)
}

func getBookByID(c *fiber.Ctx) error {
    id := c.Params("id")
    for _, b := range books {
        if b.ID == id {
            return c.JSON(b)
        }
    }
    return c.Status(fiber.StatusNotFound).JSON(fiber.Map{"message": "book not found"})
}

func createBook(c *fiber.Ctx) error {
    var book Book
    if err := c.BodyParser(&book); err != nil {
        return err
    }
    books = append(books, book)
    return c.Status(fiber.StatusCreated).JSON(book)
}

func updateBook(c *fiber.Ctx) error {
    id := c.Params("id")
    var updated Book
    if err := c.BodyParser(&updated); err != nil {
        return err
    }
    for i, b := range books {
        if b.ID == id {
            books[i] = updated
            return c.JSON(updated)
        }
    }
    return c.Status(fiber.StatusNotFound).JSON(fiber.Map{"message": "book not found"})
}

func deleteBook(c *fiber.Ctx) error {
    id := c.Params("id")
    for i, b := range books {
        if b.ID == id {
            books = append(books[:i], books[i+1:]...)
            return c.JSON(fiber.Map{"message": "book deleted"})
        }
    }
    return c.Status(fiber.StatusNotFound).JSON(fiber.Map{"message": "book not found"})
}
