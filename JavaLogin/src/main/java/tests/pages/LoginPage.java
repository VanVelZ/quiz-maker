package tests.pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class LoginPage {

    @FindBy(id = "loginField")
    private WebElement loginField;

    @FindBy(id = "passField")
    private WebElement passField;

    @FindBy(id = "loginButton")
    private WebElement loginButton;


    public LoginPage(WebDriver driver) {
        PageFactory.initElements(driver, this);
    }

    public void enterLoginInfo(String loginId) {
        this.loginField.sendKeys(loginId);
    }
    public void enterPasswordInfo(String password) {
        this.passField.sendKeys(password);
    }

    public void clickLoginButton() {
        this.loginButton.click();
    }


}
