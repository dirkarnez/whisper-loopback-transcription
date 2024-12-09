            buffer.close();
 
            whisper_full_params wparams = whisper_full_default_params(WHISPER_SAMPLING_GREEDY);
            wparams.translate = false;
            if (whisper_full(ctx, wparams, (float*)buffer.buffer().constData(), buffer.size() / 4) == 0)
            {
              std::string text;
              const int n_segments = whisper_full_n_segments(ctx);
              for (int i = 0; i < n_segments; ++i)
                text += whisper_full_get_segment_text(ctx, i);
 
              label->setText(QString::fromStdString(text));
            }