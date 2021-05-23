package controllers;

import com.google.gson.Gson;
import io.javalin.http.Handler;
import models.Login;
import models.User;
import repositories.LoginRepo;
import service.LoginService;

public class LoginController {

    private LoginService ls;
    private final Gson gson = new Gson();

    public LoginController(LoginService loginService) {
        this.ls = loginService;
    }

    public Handler login = (context) -> {
        Login login = gson.fromJson(context.body(), Login.class);
        User user = ls.userLogin(login.loginId, login.password);
        context.result(gson.toJson(user));
    };
}

