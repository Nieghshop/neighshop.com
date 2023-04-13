<?php
// Get form data
$name = $_POST['name'];
$email = $_POST['email'];
$phone = $_POST['phone'];
$org = $_POST['org'];

$contest = isset($_POST['contest']) ? 'yes' : 'no';

// Create a new row of data for the Excel sheet
$newRow = array($name, $phone, $email,  $org, $contest);

// Open the Excel file
$excelFile = fopen('abhikalp.xlsx', 'a');

// Add the new row of data to the Excel sheet
fputcsv($excelFile, $newRow);

// Close the Excel file
fclose($excelFile);

// Show a confirmation message to the user
echo "Thank you for registering! Your information has been saved.";
ini_set('display_errors', 1);
error_reporting(E_ALL);

?>
