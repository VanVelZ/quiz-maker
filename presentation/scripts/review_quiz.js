function logout(event) {

    event.preventDefault()
    console.log("logout")

    window.location.href = "///Users/alexjones/Desktop/RevatureTraining/Project2/presentation/index.html"
    clearCookie([userId])
}