from setuptools import setup, find_packages

setup(
    name='voice_translator_ultimate_plus',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'faster-whisper',
        'transformers',
        'TTS',
        'sounddevice',
        'PyQt5',
        'webrtcvad',
        'numpy',
        'lingua-language-detector',
    ],
    entry_points={
        'console_scripts': [
            'voice-translator=real_time_translator:main_loop',
        ]
    },
    include_package_data=True,
    description='Real-time speech translation with offline TTS and GUI',
    author='Your Name',
    license='MIT',
)

