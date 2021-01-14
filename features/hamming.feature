Feature: Hamming

  Scenario: Two empty strands
    Given there is a hamming class
    When we calculate distance between two empty strands
    Then the result is 0

  Scenario: Two identical single-letter strands
    Given there is a hamming class
    When we calculate distance between two identical single letter strands
    Then the result is 0

  Scenario: Two different single-letter strands
    Given there is a hamming class
    When we calculate distance between two different single letter strands
    Then the result is 1

  Scenario: Two different long strands
    Given there is a hamming class
    When we calculate distance between two different long strands
    Then the result is 9

  Scenario: Two identical long strands
    Given there is a hamming class
    When we calculate distance between two identical long strands
    Then the result is 0

  Scenario: two strands and first is longer
    Given there is a hamming class
    When we calculate distance between two strands and first is longer
    Then the result is Values cannot be of different length

  Scenario: two strands and second is longer
    Given there is a hamming class
    When we calculate distance between two strands and second is longer
    Then the result is Values cannot be of different length

  Scenario: two strands and first is empty
    Given there is a hamming class
    When we calculate distance between two strands and first is empty
    Then the result is Values cannot be of different length