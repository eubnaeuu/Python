package application;
	
import java.io.IOException;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;


public class Main2 extends Application {

	@Override
	public void start(Stage primaryStage) {
		AnchorPane root;
		try {
			root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main2.fxml"));
			primaryStage.setTitle("Application"); 
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			
			Label lbl = (Label) scene.lookup("#lblId");
			Button btn = (Button) scene.lookup("#btnId");
			
			btn.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					int lblvalue = Integer.valueOf(lbl.getText());
					lblvalue++;
					lbl.setText(lblvalue+"");
					
					// 라밸생성
					Label label = new Label("라밸no"+lblvalue);
					// 라벨요소 집어넣기
					root.getChildren().add(label);
				}
			} );
			
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} 
	}
	
	public static void main(String[] args) {
		launch(args);
	}
	
}
