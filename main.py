import numpy as np
import scipy.io.wavfile as wavfile
import scipy.fft as fft
from os import listdir

# derivative and wav conversion code written by
# https://www.tiktok.com/@tokiesan 
# mega huge shoutout

def fft_derivative(audio_data, sample_rate):
    freq_domain = fft.fft(audio_data)
    freqs = fft.fftfreq(len(audio_data), 1/sample_rate)
    freq_derivative = 1j * freqs * freq_domain
    time_domain_derivative = fft.ifft(freq_derivative)

    return np.real(time_domain_derivative)

def fft_integral(audio_data, sample_rate):
    freq_domain = fft.fft(audio_data)
    freqs = fft.fftfreq(len(audio_data), 1/sample_rate)
    integral_freqs = np.copy(freqs)
    integral_freqs[integral_freqs == 0] = np.inf
    freq_integral = np.zeros_like(freq_domain, dtype=complex)
    valid_indices = integral_freqs != np.inf # there is probs a much smarter way of going about this but idc it works
    freq_integral[valid_indices] = freq_domain[valid_indices] / (1j * integral_freqs[valid_indices])
    time_domain_integral = fft.ifft(freq_integral)

    return np.real(time_domain_integral)

def convert_file(song_file, out_file): 
    sample_rate, audio_data = wavfile.read(song_file)
    if len(audio_data.shape) == 2:
        audio_data = np.mean(audio_data, axis=1)
    
    derivative = fft_derivative(audio_data, sample_rate)
    derivative = np.int16(derivative / np.max(np.abs(derivative)) * 32767) # here is derivative list values if you want to plot or something
    integral = fft_integral(audio_data, sample_rate)
    integral = np.int16(integral / np.max(np.abs(integral)) * 32767)
    wavfile.write(out_file, sample_rate, derivative)
    wavfile.write("integral.wav", sample_rate, integral)

if __name__ == "__main__":

    youtube_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" # keep empty if you want to skip download
    SONG_FILE = "song.wav"
    OUTPUT_FILE = "derivative.wav"
    # INTEGRAL_FILE = "integral.wav"

    if youtube_link:
        if SONG_FILE in listdir():
            input("Song file already present inside directory, sure you want to continue? (hit enter to continue)")

        print("Importing Youtube DLP to download song...")
        import yt_dlp # importing here so that you don't need this package if you already have a file

        ydl_opts = {
            'outtmpl': SONG_FILE.replace(".wav", ""),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
            }]
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            error_code = ydl.download(youtube_link)

    if SONG_FILE in listdir():
        if not OUTPUT_FILE:
            OUTPUT_FILE = "output.wav"
        print("Beginning FFT")
        convert_file(SONG_FILE, OUTPUT_FILE)

    else:
        print("Process Failed: Song file not found in current directory")
