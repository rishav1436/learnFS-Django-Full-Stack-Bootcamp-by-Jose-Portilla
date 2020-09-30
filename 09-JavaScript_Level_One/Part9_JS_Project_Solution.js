fname = prompt("Enter your first name:").toLowerCase()
lname = prompt("Enter your last name:").toLowerCase()
age = prompt("Enter your age")
height = prompt("Enter your height")
pet = prompt("Enter your pet's name").toLowerCase()

if ((fname[0] === lname[0]) && (age > 20 && age < 30) && height >= 170 && pet.endsWith("y")) {
    console.log("I caught a spy!")
}