package tests;

import models.User;
import org.testng.Assert;
import org.testng.annotations.Test;
import repositories.LoginRepo;

public class LoginRepoTest {

    @Test
    public void loginTest(){
        LoginRepo lr = new LoginRepo();

        User user = new User(lr.userLogin("100000", "password"));

        Assert.assertEquals(user.userId, 1);
    }
}
