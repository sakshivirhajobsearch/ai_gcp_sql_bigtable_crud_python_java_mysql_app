package com.ai.gcp.sql.bigtable.config;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

public class ConfigReader {
	
	private static Properties props = new Properties();

	static {
		try {
			FileInputStream in = new FileInputStream("./config.properties");
			props.load(in);
		} catch (IOException e) {
			System.out.println("Error loading config: " + e.getMessage());
		}
	}

	public static String get(String key) {
		return props.getProperty(key);
	}
}
