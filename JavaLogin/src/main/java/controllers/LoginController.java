package controllers;

import com.google.gson.Gson;
import io.javalin.http.Handler;
import models.Login;
import models.User;
import repositories.LoginRepo;

public class LoginController {

    private LoginRepo lr;
    private final Gson gson = new Gson();

    public LoginController(LoginRepo loginRepo) {
        this.lr = loginRepo;
    }

    public Handler login = (context) -> {
        Login login = gson.fromJson(context.body(), Login.class);
        User user = lr.userLogin(login.loginId, login.password);
        context.result(gson.toJson(user));
    };
}

