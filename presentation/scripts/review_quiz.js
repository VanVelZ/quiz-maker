function logout(event) {

    event.preventDefault()
    console.log("logout")

    clearCookie([userId])

    window.location.href = "///Users/alexjones/Desktop/RevatureTraining/Project2/presentation/index.html"
}