package tests.behavior;

import cucumber.api.CucumberOptions;
import cucumber.api.testng.AbstractTestNGCucumberTests;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.safari.SafariDriver;
import org.openqa.selenium.safari.SafariOptions;
import org.testng.annotations.AfterSuite;
import org.testng.annotations.BeforeSuite;
import tests.pages.LoginPage;

@CucumberOptions(
        features = {"src/main/java/tests/resources/loginPage.feature"},
        glue = {"tests.steps"})
public class LoginRunner extends AbstractTestNGCucumberTests {

    public static WebDriver driver;
    public static LoginPage loginPage;


    @BeforeSuite
    public void setUp() {

        SafariOptions options = new SafariOptions();

        driver = new SafariDriver(options);
        loginPage = new LoginPage(driver);
    }

    @AfterSuite
    public void tearDown() {
        driver.quit();

    }

}
