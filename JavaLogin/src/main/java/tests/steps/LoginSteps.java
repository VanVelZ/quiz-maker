package tests.steps;

import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;
import org.openqa.selenium.WebDriver;
import tests.behavior.LoginRunner;
import tests.pages.LoginPage;

public class LoginSteps {

    public static WebDriver driver = LoginRunner.driver;
    public static LoginPage loginPage = LoginRunner.loginPage;

    @Given("^The user is on the login screen$")
    public void the_user_is_on_the_login_screen(){
        driver.get("file:///Users/prozachrx/Desktop/quiz-maker/presentation/index.html");

    }

    @When("^The user enters \"([^\"]*)\" in the username input$")
    public void the_user_enters_in_the_username_input(String arg1) {
        loginPage.enterLoginInfo(arg1);
    }

    @When("^The user enters \"([^\"]*)\" in the password input$")
    public void the_user_enters_in_the_password_input(String arg1) {
        loginPage.enterPasswordInfo(arg1);
    }

    @When("^The user hits the submit button$")
    public void the_user_hits_the_submit_button() {
        loginPage.clickLoginButton();
    }

    @Then("^The user is redirected the main page$")
    public void the_user_is_redirected_the_main_page() {
        assert !driver.getTitle().equals("Login");
    }

}
