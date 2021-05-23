package repositories;

import models.User;
import util.JDBC;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class LoginRepo {
    public static Connection conn = JDBC.getConnection();

    public User userLogin(String loginId, String password) {
        try {
            String sql = "SELECT id, role_id FROM users WHERE login_id = ? and password = ?";

            PreparedStatement ps = conn.prepareStatement(sql);
            ps.setString(1, loginId);
            ps.setString(2, password);

            ResultSet rs = ps.executeQuery();

            if (rs.next()) {
                int userId = rs.getInt("id");
                int roleId = rs.getInt("role_id");
                return new User(userId, roleId);
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }

        return null;
    }

}

