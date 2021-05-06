package application;
	
import java.io.IOException;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;


public class Main7 extends Application {

	@Override
	public void start(Stage primaryStage) {
		AnchorPane root;
		try {
			root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main7.fxml"));
			primaryStage.setTitle("Application"); 
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			
			Button btn = (Button)scene.lookup("#btn");
			TextField tfmine = (TextField)scene.lookup("#tfmine");
			TextField tfcom = (TextField)scene.lookup("#tfcom");
			TextField tfresult = (TextField)scene.lookup("#tfresult");
			
			btn.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					double tmp = Math.random();
					System.out.println(tmp);
					String mineans = tfmine.getText(); 
					String comans = "";
					
					if(tmp<(double)(1/3)) {
						comans = "가위";
					} else if(tmp <(double)(2/3)){
						comans = "바위";
					} else {
						comans = "보";
					}
					
					tfcom.setText(comans); 
					
					String result = gababo(mineans, comans);
					tfresult.setText(result);
					
				}
			});
			
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch (IOException e) {
			e.printStackTrace();
		} 
	}
	
	
	public String gababo(String str1, String str2) {
		
		String result ="";
		
		if(str1.equals("가위") && str2.equals("가위")) result = "비김";
		if(str1.equals("가위") && str2.equals("바위")) result = "짐";
		if(str1.equals("가위") && str2.equals("보")) result = "이김";
		
		if(str1.equals("바위") && str2.equals("가위")) result = "이김";
		if(str1.equals("바위") && str2.equals("바위")) result = "비김";
		if(str1.equals("바위") && str2.equals("보")) result = "짐";
			
		if(str1.equals("보") && str2.equals("가위")) result = "짐";
		if(str1.equals("보") && str2.equals("바위")) result = "이김";
		if(str1.equals("보") && str2.equals("보")) result = "비김";
		
		return result;
	}
	public static void main(String[] args) {
		launch(args);
	}
	
}
