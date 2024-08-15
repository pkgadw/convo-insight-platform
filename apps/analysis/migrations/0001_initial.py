# Generated by Django 5.0.7 on 2024-08-15 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConversationMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overall_satisfaction_score', models.FloatField(blank=True, null=True)),
                ('average_response_time', models.DurationField(blank=True, null=True)),
                ('average_accuracy_score', models.FloatField(blank=True, null=True)),
                ('average_relevance_score', models.FloatField(blank=True, null=True)),
                ('feedback', models.TextField(blank=True)),
                ('evaluated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='IntentPrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confidence_score', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='LLMAgentPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_time', models.DurationField()),
                ('accuracy_score', models.FloatField(blank=True, null=True)),
                ('relevance_score', models.FloatField(blank=True, null=True)),
                ('customer_satisfaction_score', models.FloatField(blank=True, null=True)),
                ('quality_score', models.FloatField(blank=True, null=True)),
                ('feedback', models.TextField(blank=True)),
                ('evaluated_at', models.DateTimeField(auto_now_add=True)),
                ('issue_resolved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('confidence_score', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('applied', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TopicDistribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
            ],
        ),
    ]
