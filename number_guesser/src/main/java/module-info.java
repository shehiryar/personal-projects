module com.example.number_guesser {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.desktop;


    opens com.example.number_guesser to javafx.fxml;
    exports com.example.number_guesser;
}