package com.ai.gcp.sql.bigtable.repository;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class MySQLLogRepository {

	public static List<String> fetchLogs() {

		List<String> logs = new ArrayList<>();
		try {
			Connection conn = DriverManager
					.getConnection("jdbc:mysql://localhost:3306/ai_gcp_sql_bigtable?useSSL=false", "root", "admin");

			Statement stmt = conn.createStatement();
			ResultSet rs = stmt.executeQuery("SELECT * FROM analysis_logs ORDER BY timestamp DESC");

			while (rs.next()) {
				logs.add(String.format("[%s] Source: %s, Records: %d, Anomalies: %d, Status: %s",
						rs.getTimestamp("timestamp"), rs.getString("source"), rs.getInt("record_count"),
						rs.getInt("anomaly_count"), rs.getString("status")));
			}

			rs.close();
			stmt.close();
			conn.close();
		} catch (SQLException e) {
			logs.add("Error: " + e.getMessage());
		}
		return logs;
	}
}
