package com.ai.gcp.sql.bigtable.repository;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

import com.ai.gcp.sql.bigtable.config.ConfigReader;

public class GCPBigtableRepository {
	
	public static String fetchData() {
		
		StringBuilder result = new StringBuilder();
		try {
			String baseUrl = ConfigReader.get("api.baseurl");
			String endpoint = ConfigReader.get("api.endpoint.bigtable");
			URL url = new URL(baseUrl + endpoint);
			HttpURLConnection conn = (HttpURLConnection) url.openConnection();
			conn.setRequestMethod("GET");

			BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
			String line;
			while ((line = in.readLine()) != null)
				result.append(line).append("\n");
			in.close();
		} catch (Exception e) {
			result.append("Error: ").append(e.getMessage());
		}
		return result.toString();
	}
}
