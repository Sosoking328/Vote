package com.sosokan.android.events.Listener;

import com.google.android.youtube.player.YouTubePlayer;

/**
 * Created by AnhZin on 8/25/2016.
 */
public final class MyPlaybackEventListener implements YouTubePlayer.PlaybackEventListener {

    @Override
    public void onPlaying() {
        // Called when playback starts, either due to user action or call to play().
        //showMessage("Playing");
    }

    @Override
    public void onPaused() {
        // Called when playback is paused, either due to user action or call to pause().
       // showMessage("Paused");
    }

    @Override
    public void onStopped() {
        // Called when playback stops for a reason other than being paused.
      //  showMessage("Stopped");
    }

    @Override
    public void onBuffering(boolean b) {
        // Called when buffering starts or ends.
    }

    @Override
    public void onSeekTo(int i) {
        // Called when a jump in playback position occurs, either
        // due to user scrubbing or call to seekRelativeMillis() or seekToMillis()
    }
}