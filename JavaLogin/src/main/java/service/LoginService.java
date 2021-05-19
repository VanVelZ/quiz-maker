package service;

import models.User;
import repositories.LoginRepo;


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


