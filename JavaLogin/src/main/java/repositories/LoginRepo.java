package repositories;

import util.JDBC;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class LoginRepo {
    public static Connection conn = JDBC.getConnection();

    public int getMovie(String loginId, String password) {
        try {
            String sql = "SELECT id FROM users WHERE login_id = ? and password = ?";

            PreparedStatement ps = conn.prepareStatement(sql);
            ps.setString(1, loginId);
            ps.setString(2, password);

            ResultSet rs = ps.executeQuery();

            if (rs.next()) {
                return rs.getInt("id");
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }

        return -1;
    }

}

