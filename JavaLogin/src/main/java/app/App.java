package app;

import controllers.LoginController;
import io.javalin.Javalin;
import repositories.LoginRepo;

public class App {

    public static void main(String[] args) {

        Javalin app = Javalin.create(config -> config.enableCorsForAllOrigins());
        establishRoutes(app);

        app.start(7001);

    }

    public static void establishRoutes(Javalin app) {
        LoginRepo lr = new LoginRepo();
        LoginController lc = new LoginController(lr);
        app.post("/login", lc.login);

    }


}
