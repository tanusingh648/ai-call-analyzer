analyzeBtn.setOnClickListener(v -> {
    status.setText("Listening...");
    startSpeechRecognition();
});
if (risk > 60) {
    riskText.setText("🚨 Risk: " + risk + "%");
    rootLayout.setBackgroundColor(Color.RED);
    vibratePhone();
} else {
    riskText.setText("✅ Safe Call");
    rootLayout.setBackgroundColor(Color.GREEN);
}
