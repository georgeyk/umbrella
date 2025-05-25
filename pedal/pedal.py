import marimo

__generated_with = "0.13.11"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from pedalboard import Pedalboard, Chorus, Compressor, Delay, Gain, Reverb, Phaser, PitchShift, Mix, NoiseGate
    from pedalboard.io import AudioStream
    return (
        AudioStream,
        Chorus,
        Gain,
        NoiseGate,
        Pedalboard,
        PitchShift,
        Reverb,
        mo,
    )


@app.cell
def _(AudioStream, mo):
    inputs = mo.ui.dropdown(
        options=AudioStream.input_device_names, label="choose one"
    )
    inputs
    return (inputs,)


@app.cell
def _(AudioStream, mo):
    outputs = mo.ui.dropdown(options=AudioStream.output_device_names, label="choose one")
    outputs
    return (outputs,)


@app.cell
def _(
    AudioStream,
    Chorus,
    Gain,
    NoiseGate,
    Pedalboard,
    PitchShift,
    Reverb,
    inputs,
    outputs,
):
    if inputs.selected_key and outputs.selected_key:
        stream = AudioStream(
            input_device_name=inputs.selected_key,
            output_device_name=outputs.selected_key,
            num_input_channels=2,
            num_output_channels=2,
            allow_feedback=True,
            buffer_size=128,
            sample_rate=44100,
        )

        stream.plugins = Pedalboard(
            [
                NoiseGate(),
                #PitchShift(semitones=-5),
                PitchShift(semitones=12),
                Gain(gain_db=6),
                Reverb(0.1), 
                Chorus()
            ]
        )

        stream.run()
    return


if __name__ == "__main__":
    app.run()
