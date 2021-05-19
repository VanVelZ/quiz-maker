package service;

import models.Login;
import models.User;
import org.apache.commons.logging.Log;
import repositories.LoginRepo;

import java.util.List;

public class LoginService {
    public LoginRepo lr;


    public LoginService(){
        lr = new LoginRepo();
    }
    public LoginService(LoginRepo lr) {
        this.lr = lr;
    }

    public User userLogin(String loginId, String password) {
        return lr.userLogin(loginId, password);
    }

}


