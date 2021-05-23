package tests.steps;

import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import tests.behavior.LoginRunner;
import tests.pages.LoginPage;

import java.util.concurrent.TimeUnit;

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
    public void the_user_is_redirected_the_main_page() throws InterruptedException {
        //Titles are always on the screen so I couldnt find a better strategy than sleeping
        Thread.sleep(1000);
        assert !driver.getTitle().equals("Quiz Maker");
    }

}
