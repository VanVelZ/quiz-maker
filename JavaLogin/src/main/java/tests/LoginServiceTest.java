package tests;

import models.User;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.MockitoAnnotations;
import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import repositories.LoginRepo;
import service.LoginService;

public class LoginServiceTest {

    @Mock
    public LoginRepo loginRepo;

    @InjectMocks
    public LoginService loginService;


    @BeforeClass
    public void setUp() {
        loginRepo = new LoginRepo();
        loginService = new LoginService(loginRepo);

        MockitoAnnotations.initMocks(this);
    }

    @Test
    public void loginSuccess() {

        String loginId = "200000";
        String password = "password";
        User user = new User(1, 1);

        Mockito.when(loginRepo.userLogin(loginId, password)).thenReturn(user);

        Assert.assertEquals(user.userId, new User(1, 1).userId);

    }

}
