CREATE DATABASE FraudAware;

USE FraudAware;

CREATE TABLE scam_keywords(
id INT AUTO_INCREMENT PRIMARY KEY,
keyword VARCHAR(100),
weight INT
);

CREATE TABLE safe_keywords(
id INT AUTO_INCREMENT PRIMARY KEY,
keyword VARCHAR(100)
);

INSERT INTO scam_keywords 
(keyword, weight)
VALUES 
('click here', 2),
('win', 2),
('congratulations', 2),
('urgent', 1),
('blocked', 1),
('verify', 1),
('claim now', 2),
('limited time', 1),
('OTP', 1),
('lottery', 2),
('prize', 2);

INSERT INTO safe_keywords (keyword) VALUES
('netbanking'),
('gov.in'),
('official site'),
('secure login'),
('electricity board');

CREATE TABLE quiz_questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message TEXT,
    correct_answer VARCHAR(10) -- 'Scam' or 'Real'
);

TRUNCATE TABLE  quiz_questions;

ALTER TABLE quiz_questions
ADD COLUMN explanation TEXT;

INSERT INTO quiz_questions (message, correct_answer, explanation) VALUES
(
  "Your bank account has been blocked. Click here to verify: bit.ly/verify123",
  "Scam",
  "Scammers often use urgency and shortened links to trick users into clicking harmful websites."
),
(
  "Congratulations! You've won ₹50,000. Claim now: freeprize.com",
  "Scam",
  "Prize scams use fake offers and unknown URLs to lure users into sharing personal data."
),
(
  "Reminder: Your credit card bill is due on the 5th. Log in to netbanking to pay.",
  "Real",
  "Typical bank reminders don’t contain suspicious links or pressure tactics."
),
(
  "Your income tax refund has been processed. Visit the official site to track it.",
  "Real",
  "It references a legitimate government process without demanding immediate action."
),
(
  "Limited time offer! Win an iPhone now: promo.in/gift",
  "Scam",
  "Unsolicited offers with unknown links and urgency are signs of phishing scams."
),
(
  "Electricity bill paid successfully. Thank you for using ABC services.",
  "Real",
  "A standard confirmation message from a service provider, with no suspicious elements."
),
(
  "Urgent: Verify your UPI ID to avoid suspension",
  "Scam",
  "Scam messages often use fear and threats like suspension to provoke a response."
),
(
  "IRCTC ticket booked successfully. Happy journey!",
  "Real",
  "This is a typical transactional message from a verified source (IRCTC)."
);
SET SQL_SAFE_UPDATES = 0;
DELETE FROM quiz_questions WHERE message IS NULL OR correct_answer IS NULL OR explanation IS NULL;

SELECT * FROM quiz_questions;

INSERT INTO quiz_questions (message, correct_answer, explanation) VALUES
("Win ₹1 lakh cash today! Click fast before the offer ends: winbig.in", "Scam", "The message creates urgency and includes a suspicious URL."),
("Your Aadhaar is successfully linked to your bank account.", "Real", "This is a confirmation message without any links or urgency."),
("Dear user, your SIM will be blocked in 2 hours if not verified: verify-now.site", "Scam", "Threat of blocking and non-official link indicates a phishing scam."),
("Reminder: Your FASTag has low balance. Recharge via your bank app.", "Real", "It's a standard balance alert without any suspicious elements."),
("Get FREE investment tips from experts. Join our Telegram group now!", "Scam", "Scam messages often lure victims with free offers and redirect to risky platforms.");
