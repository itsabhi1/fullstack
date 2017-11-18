package com.example.android.footballgame;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {
    int scoreIndia=0;
    int scorePakistan=0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    public void increment4A(View view)
    {
        scoreIndia +=4;
        displayA(scoreIndia);
    }
    public void increment6A(View view)
    {
        scoreIndia +=6;
        displayA(scoreIndia);
    }
    public void NoBallI(View view)
    {
        scoreIndia +=1;
        displayA(scoreIndia);
    }
    public void displayA(int number)
    {
        val scoreTextView=findViewById(R.id.scoreIndia);
        scoreTextView.text ="$number";
    }
    public void increment4B(View view)
    {
        scorePakistan +=4;
        displayB(scorePakistan);
    }
    public void increment6B(View view)
    {
        scorePakistan +=6;
        displayB(scorePakistan);
    }
    public void NoBallP(View view)
    {
        scorePakistan +=1;
    }
    public void displayB(int number)
    {
        val scoreTextView=findViewById(R.id.scorePakistan);
        scoreTextView.text="$number";
    }
    public void reset(View view)
    {
        scoreIndia=0;
        scorePakistan=0;
        displayReset(scoreIndia,scorePakistan);
    }
    public void displayReset(int num1,int num2)
    {
        val scoreTextViewA=findViewById(R.id.scoreIndia);
        scoreTextViewA.text = "$num1";
        val scoreTextViewB=findViewById(R.id.scoreIndia);
        scoreTextViewB.text = "$num2";
    }
}
