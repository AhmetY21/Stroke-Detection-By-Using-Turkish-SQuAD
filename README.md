# Stroke-Detection-By-Using-Turkish-SQuAD
This repo contains codes and other materials developed by Enes Tel, Eren Göksu & myself for @Hack4Treat Hackathon.

## StrokeShield

StrokeShield is the decision support system that investigates the risk for a stroke of each patient and then informs about the risk to healthcare workers. It uses NLP for analysing the anamnesis of a patient to detect whether there are specific risk factors are present or not.

### Background Info & Aim of the Project

Anamnesis is a detailed long text format healthcare record that includes the medical story of the patient. Healthcare workers have to record anamnesis of each patient when they come to the hospital for an illness. However, due to rush nature of the healthcare systems or the depends on the services, doctors might miss realising the risk factors for stroke. 

We aim to find the answers to questions like neurologists for revealing the stroke risk of a patient.

### Questions for Stroke Risk

20+ questions are written by the @Enes_Tel after  long hours of detailed research about the stroke and several interviews with the neurologists. The questions and the possible answer types can be found in the Questions.xlsx document. 

### Question Anserwering for Turkish Documents
 
We have used savasy/bert-base-turkish-squad model which is a fine tuned bert based model. This model helps us to narrow down the context, and then find out the answers by using modified search functions.




