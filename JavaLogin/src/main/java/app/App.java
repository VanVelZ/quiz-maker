package app;

import controllers.LoginController;
import io.javalin.Javalin;
import repositories.LoginRepo;
import service.LoginService;

public class App {

    public static void main(String[] args) {

        Javalin app = Javalin.create(config -> config.enableCorsForAllOrigins());
        establishRoutes(app);

        app.start(7001);

    }

    public static void establishRoutes(Javalin app) {
        LoginService ls = new LoginService();
        LoginController lc = new LoginController(ls);
        app.post("/login", lc.login);

    }


}
