package application;
	
import java.io.IOException;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;


public class Main8 extends Application {

	@Override
	public void start(Stage primaryStage) {
		AnchorPane root;
		try {
			root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main8.fxml"));
			primaryStage.setTitle("Application"); 
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			
			Button btn = (Button)scene.lookup("#btn");
			TextField tf = (TextField)scene.lookup("#tf");
			TextArea ta = (TextArea)scene.lookup("#ta");
			
			btn.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					int dan = Integer.valueOf(tf.getText());
					String tmp ="";
					for(int i = 1; i<10; i++) {
						tmp += dan + "x" + i + "=" + dan*i + "\n";
					}
					ta.setText(tmp);
					
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
