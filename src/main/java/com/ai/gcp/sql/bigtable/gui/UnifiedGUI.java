package com.ai.gcp.sql.bigtable.gui;

import java.util.List;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

import com.ai.gcp.sql.bigtable.repository.GCPBigtableRepository;
import com.ai.gcp.sql.bigtable.repository.GCPCloudSQLRepository;
import com.ai.gcp.sql.bigtable.repository.MySQLLogRepository;

public class UnifiedGUI {

	public static void main(String[] args) {

		JFrame frame = new JFrame("GCP SQL & Bigtable Dashboard");
		JButton btnSQL = new JButton("Load Cloud SQL");
		JButton btnBigtable = new JButton("Load Bigtable");
		JButton btnLogs = new JButton("Show AI Logs");
		JTextArea output = new JTextArea(25, 80);

		btnSQL.addActionListener(e -> {
			String response = GCPCloudSQLRepository.fetchData();
			output.setText(response);
		});

		btnBigtable.addActionListener(e -> {
			String response = GCPBigtableRepository.fetchData();
			output.setText(response);
		});

		btnLogs.addActionListener(e -> {
			List<String> logs = MySQLLogRepository.fetchLogs();
			output.setText(String.join("\n", logs));
		});

		JPanel panel = new JPanel();
		panel.add(btnSQL);
		panel.add(btnBigtable);
		panel.add(btnLogs);
		panel.add(new JScrollPane(output));

		frame.add(panel);
		frame.pack();
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setVisible(true);
	}
}
