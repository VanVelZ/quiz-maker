package controllers;

import com.google.gson.Gson;
import io.javalin.http.Handler;
import repositories.LoginRepo;

public class LoginController {

    private LoginRepo lr;
    private Gson gson = new Gson();

    public LoginController(LoginRepo loginRepo) {
        this.lr = loginRepo;
    }

    public Handler login = (context) -> {
        String loginId = context.pathParam("loginId");
        String password = context.pathParam("password");
        int id = lr.userLogin(loginId, password);
        context.result(gson.toJson(id));
    };


}

