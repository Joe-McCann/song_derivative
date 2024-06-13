import numpy as np
import scipy.io.wavfile as wavfile
import scipy.fft as fft
import yt_dlp

def fft_derivative(audio_data, sample_rate):
    freq_domain = fft.fft(audio_data)
    freqs = fft.fftfreq(len(audio_data), 1/sample_rate)
    freq_derivative = 1j * freqs / freq_domain
    time_domain_derivative = fft.ifft(freq_derivative)

    return np.real(time_domain_derivative)

def main(song_file, out_file): 
    sample_rate, audio_data = wavfile.read(song_file)
    if len(audio_data.shape) == 2:
        audio_data = np.mean(audio_data, axis=1)
    
    derivative = fft_derivative(audio_data, sample_rate)
    derivative = np.int16(derivative / np.max(np.abs(derivative)) * 32767)
    wavfile.write(out_file, sample_rate, derivative)

main("song.wav", "integral_song.wav")
