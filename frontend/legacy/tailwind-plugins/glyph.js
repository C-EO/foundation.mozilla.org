const plugin = require("tailwindcss/plugin");

const defaultGlyphPath = "../_images/glyphs";

function glyph(
  id,
  pathToDirectory = defaultGlyphPath,
  width = "20px",
  height = "20px"
) {
  return {
    "&::before": {
      content: "''",
      display: "inline-block",
      width: width,
      height: height,
      marginRight: "20px",
      background: `url(${pathToDirectory}/${id}.svg) no-repeat 0 0 / contain`,
      "@media (min-width: 992px)": {
        "&": {
          marginRight: "10px",
        },
      },
    },
  };
}

function hoverGlyph(id, pathToDirectory = defaultGlyphPath) {
  return {
    "&:hover::before, &:focus::before": {
      background: `url(${pathToDirectory}/${id}.svg) no-repeat 0 0 / contain`,
    },
  };
}

module.exports = [
  plugin(function ({ addComponents }) {
    // Using Same breakpoints for containers as bootstrap
    addComponents([
      {
        ".heart-glyph": {
          ...glyph("heart"),
          ...hoverGlyph("heart-hover"),
          "&:before": {
            width: "19px",
            height: "16px",
            marginRight: "6px",
            position: "relative",
            top: "2px",
          },
          // Hover and active before
          "&:hover::before, &:focus::before": {
            filter: "brightness(0) invert(100%)",
          },
        },
        ".donate": {
          ...glyph("donate"),
        },
        ".twitter-glyph": {
          ...glyph("twitter"),
          ...hoverGlyph("twitter-hover"),
          "&:before": {
            width: "16px",
            height: "16px",
          },
        },
        ".linkedin-glyph": {
          ...glyph("linkedin"),
          ...hoverGlyph("linkedin-hover"),
          "&:before": {
            width: "16px",
            height: "18px",
          },
        },
        ".tiktok-glyph": {
          ...glyph("tiktok"),
          ...hoverGlyph("tiktok-hover"),
          "&:before": {
            width: "16px",
            height: "16px",
          },
        },
        ".bluesky-glyph": {
          ...glyph("bluesky"),
          ...hoverGlyph("bluesky-hover"),
          "&:before": {
            width: "16px",
            height: "16px",
          },
        },
        ".form-error-glyph": {
          ...glyph("form-error"),
          display: "flex",
          "&:before": {
            width: "13px",
            height: "13px",
            marginRight: "10px",
          },
        },
        ".dark": {
          "& .twitter-glyph": {
            ...glyph("twitter-dark-theme"),
            ...hoverGlyph("twitter-dark-theme-hover"),
            "&:before": {
              width: "16px",
              height: "16px",
            },
          },
          "& .instagram-glyph": {
            ...glyph("instagram-dark-theme"),
            ...hoverGlyph("instagram-dark-theme-hover"),
            "&:before": {
              width: "16px",
              height: "16px",
            },
          },
          "& .medium-glyph": {
            ...glyph("medium-dark-theme"),
            ...hoverGlyph("medium-dark-theme-hover"),
          },
          "& .youtube-glyph": {
            ...glyph("youtube-dark-theme"),
            ...hoverGlyph("youtube-dark-theme-hover"),
            "&:before": {
              width: "18px",
              height: "18px",
              marginTop: "2px",
            },
          },
          "& .email-glyph": {
            ...glyph("email-dark-theme"),
            ...hoverGlyph("email-dark-theme-hover"),
            "&:before": {
              width: "16px",
              height: "16px",
            },
          },
          "& .github-glyph": {
            ...glyph("github-dark-theme"),
            ...hoverGlyph("github-dark-theme-hover"),
            "&:before": {
              width: "16px",
              height: "16px",
            },
          },
          "& .linkedin-glyph": {
            ...glyph("linkedin-dark-theme"),
            ...hoverGlyph("linkedin-dark-theme-hover"),
            "&:before": {
              width: "16px",
              height: "18px",
            },
          },
          "& .tiktok-glyph": {
            ...glyph("tiktok-dark-theme"),
            ...hoverGlyph("tiktok-dark-theme-hover"),
            "&:before": {
              width: "16px",
              height: "16px",
            },
          },
          "& .bluesky-glyph": {
            ...glyph("bluesky-dark-theme"),
            ...hoverGlyph("bluesky-dark-theme-hover"),
            "&:before": {
              width: "16px",
              height: "16px",
            },
          },
          "& .form-error-glyph": {
            ...glyph("form-error-dark-theme"),
          },
          "& .globe-glyph": {
            ...glyph("globe-dark-theme"),
            "&:before": {
              width: "24px",
              height: "24px",
              marginRight: "10px",
            },
          },
        },
      },
    ]);
  }),
];
