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


public class Main5 extends Application {

	@Override
	public void start(Stage primaryStage) {
		AnchorPane root;
		try {
			root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main5.fxml"));
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
					if(tmp < 0.5) {
						tfcom.setText("홀");
					}else {
						tfcom.setText("짝");
					}
					
					String mine = tfmine.getText();
					String com = tfcom.getText();
					String result = "";
					
					if(mine.equals(com))
						tfresult.setText("정답");
					else
						tfresult.setText("땡!");
				}
			});
			
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch (IOException e) {
			e.printStackTrace();
		} 
	}
	
	public static void main(String[] args) {
		launch(args);
	}
	
}
