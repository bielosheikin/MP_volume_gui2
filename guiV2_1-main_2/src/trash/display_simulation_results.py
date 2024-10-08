import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def figure_plottting(result, T, dt):
    new_rc_params = {"text.usetex": False, "svg.fonttype": "none"}
    matplotlib.rcParams.update(new_rc_params)
    # ax.set_xticklabels(fontsize = 10, rotation = 0)
    t_axis2 = np.arange(0, T - dt, dt)
    t_axis = np.arange(0, T, dt)
    fig, axes = plt.subplots(3, 3, figsize=(15, 15), sharex=False)
    plt.subplots_adjust(wspace=0.55, hspace=0.6)
    matplotlib.rcParams["font.sans-serif"] = "Arial"
    matplotlib.rcParams["font.family"] = "Arial"

    axes[0, 0].plot(
        t_axis,
        result["other_variables"]["vesicle_parameters"]["pH"],
        color="#348ABD",
        linewidth=1,
    )
    axes[0, 0].set_title("pH", fontsize=20, pad=20)
    # axes[0,0].set_ylim(4.0,7.5)
    axes[0, 0].set_ylim(4.5, 8.5)
    axes[0, 0].set_xlim(0, T)
    axes[0, 0].spines["right"].set_visible(False)
    axes[0, 0].spines["top"].set_visible(False)
    axes[0, 0].spines["bottom"].set_linewidth(0.4)
    axes[0, 0].spines["left"].set_linewidth(0.4)
    axes[0, 0].spines["left"].set_position(("outward", 5))
    axes[0, 0].tick_params(axis="both", which="major", labelsize=16, width=0.2)
    axes[0, 0].set_ylabel("pH", fontname="Arial", fontsize=24)
    axes[0, 0].set_xlabel("Time, s", fontname="Arial", fontsize=24)

    axes[0, 1].plot(
        t_axis,
        result["other_variables"]["vesicle_parameters"]["V"] * 1e18,
        color="#348ABD",
        linewidth=1,
    )
    axes[0, 1].set_title("Volume", fontsize=20, pad=20)
    # axes[0,1].set_ylim(0.0,10.0)
    axes[0, 1].set_ylim(1.0, 10.0)
    axes[0, 1].set_xlim(0, T)
    axes[0, 1].spines["right"].set_visible(False)
    axes[0, 1].spines["top"].set_visible(False)
    axes[0, 1].spines["bottom"].set_linewidth(0.4)
    axes[0, 1].spines["left"].set_linewidth(0.4)
    axes[0, 1].spines["left"].set_position(("outward", 5))
    axes[0, 1].tick_params(axis="both", which="major", labelsize=16, width=0.2)
    axes[0, 1].set_ylabel(" $\mathregular{µm^3}$", fontname="Arial", fontsize=24)
    axes[0, 1].set_xlabel("Time, s", fontname="Arial", fontsize=24)

    axes[0, 2].plot(
        t_axis,
        result["other_variables"]["vesicle_parameters"]["U"] * 1000,
        color="#348ABD",
        linewidth=1,
    )
    axes[0, 2].set_title("Membrane potential", fontsize=20, pad=20)
    axes[0, 2].set_ylim(-90.0, 60.0)
    # axes[0,2].set_ylim(-80.0,40.0)
    axes[0, 2].set_xlim(0, T)
    axes[0, 2].spines["right"].set_visible(False)
    axes[0, 2].spines["top"].set_visible(False)
    axes[0, 2].spines["bottom"].set_linewidth(0.4)
    axes[0, 2].spines["left"].set_linewidth(0.4)
    axes[0, 2].spines["left"].set_position(("outward", 5))
    axes[0, 2].tick_params(axis="both", which="major", labelsize=16, width=0.2)
    axes[0, 2].set_ylabel("mV", fontname="Arial", fontsize=24)
    axes[0, 2].set_xlabel("Time, s", fontname="Arial", fontsize=24)

    axes[1, 0].plot(
        t_axis2, result["fluxes"]["Cl"]["ASOR"] * 1e18, color="#348ABD", linewidth=1
    )
    axes[1, 0].set_title("Cl$^{-}$ flux through ASOR", fontsize=20)
    # axes[1,0].set_ylim(-2.0,0.0)
    axes[1, 0].set_xlim(0, T)
    axes[1, 0].spines["right"].set_visible(False)
    axes[1, 0].spines["top"].set_visible(False)
    axes[1, 0].spines["bottom"].set_linewidth(0.4)
    axes[1, 0].spines["left"].set_linewidth(0.4)
    axes[1, 0].spines["left"].set_position(("outward", 5))
    axes[1, 0].tick_params(axis="both", which="major", labelsize=16, width=0.2)
    axes[1, 0].set_ylabel("mol*s$^{-1}$, $10^{-18}$", fontname="Arial", fontsize=24)
    axes[1, 0].set_xlabel("Time, s", fontname="Arial", fontsize=24)

    axes[1, 1].plot(
        t_axis2, result["fluxes"]["Cl"]["CLC"] * 1e19, color="#348ABD", linewidth=1
    )
    axes[1, 1].set_title("Cl$^{-}$ flux through CLC", fontsize=20)
    # axes[1,1].set_ylim(-3.5,0.1)
    axes[1, 1].set_xlim(0, T)
    axes[1, 1].spines["right"].set_visible(False)
    axes[1, 1].spines["top"].set_visible(False)
    axes[1, 1].spines["bottom"].set_linewidth(0.4)
    axes[1, 1].spines["left"].set_linewidth(0.4)
    axes[1, 1].spines["left"].set_position(("outward", 5))
    axes[1, 1].tick_params(axis="both", which="major", labelsize=16, width=0.2)
    axes[1, 1].set_ylabel("mol*s$^{-1}$, $10^{-19}$", fontname="Arial", fontsize=24)
    axes[1, 1].set_xlabel("Time, s", fontname="Arial", fontsize=24)

    axes[1, 2].plot(
        t_axis2, result["fluxes"]["H"]["CLC"] * 1e19, color="#348ABD", linewidth=1
    )
    axes[1, 2].set_title("H$^{+}$ flux through CLC", fontsize=20)
    # axes[1,2].set_ylim(-0.1,1.5)
    axes[1, 2].set_xlim(0, T)
    axes[1, 2].spines["right"].set_visible(False)
    axes[1, 2].spines["top"].set_visible(False)
    axes[1, 2].spines["bottom"].set_linewidth(0.4)
    axes[1, 2].spines["left"].set_linewidth(0.4)
    axes[1, 2].spines["left"].set_position(("outward", 5))
    axes[1, 2].tick_params(axis="both", which="major", labelsize=16, width=0.2)
    axes[1, 2].set_ylabel("mol*s$^{-1}$, $10^{-19}$", fontname="Arial", fontsize=24)
    axes[1, 2].set_xlabel("Time, s", fontname="Arial", fontsize=24)

    axes[2, 0].plot(
        t_axis2, result["fluxes"]["Na"]["TPC"] * 1e18, color="#348ABD", linewidth=1
    )
    axes[2, 0].set_title("Na$^{+}$ flux through TPC", fontsize=20)
    # axes[2,0].set_ylim(-5,0)
    axes[2, 0].set_xlim(0, T)
    axes[2, 0].spines["right"].set_visible(False)
    axes[2, 0].spines["top"].set_visible(False)
    axes[2, 0].spines["bottom"].set_linewidth(0.4)
    axes[2, 0].spines["left"].set_linewidth(0.4)
    axes[2, 0].spines["left"].set_position(("outward", 5))
    axes[2, 0].tick_params(axis="both", which="major", labelsize=16, width=0.2)
    axes[2, 0].set_ylabel("mol*s$^{-1}$, $10^{-18}$", fontname="Arial", fontsize=24)
    axes[2, 0].set_xlabel("Time, s", fontname="Arial", fontsize=24)

    axes[2, 1].plot(
        t_axis2, result["fluxes"]["H"]["vATPase"] * 1e20, color="#348ABD", linewidth=1
    )
    axes[2, 1].set_title("H$^{+}$ flux through V-ATPase", fontsize=20, pad=20)
    # axes[2,1].set_ylim(-0.1,3)
    axes[2, 1].set_xlim(0, T)
    axes[2, 1].spines["right"].set_visible(False)
    axes[2, 1].spines["top"].set_visible(False)
    axes[2, 1].spines["bottom"].set_linewidth(0.4)
    axes[2, 1].spines["left"].set_linewidth(0.4)
    axes[2, 1].spines["left"].set_position(("outward", 5))
    axes[2, 1].tick_params(axis="both", which="major", labelsize=16, width=0.2)
    axes[2, 1].set_ylabel("mol*s$^{-1}$, $10^{-20}$", fontname="Arial", fontsize=24)
    axes[2, 1].set_xlabel("Time, s", fontname="Arial", fontsize=24)

    axes[2, 2].plot(
        t_axis2, result["fluxes"]["H"]["H_leak"] * 1e20, color="#348ABD", linewidth=1
    )
    axes[2, 2].set_title("H$^{+}$ flux through H-leak", fontsize=20, pad=20)
    # axes[2,2].set_ylim(-2,3)
    axes[2, 2].set_xlim(0, T)
    axes[2, 2].spines["right"].set_visible(False)
    axes[2, 2].spines["top"].set_visible(False)
    axes[2, 2].spines["bottom"].set_linewidth(0.4)
    axes[2, 2].spines["left"].set_linewidth(0.4)
    axes[2, 2].spines["left"].set_position(("outward", 5))
    axes[2, 2].tick_params(axis="both", which="major", labelsize=16, width=0.2)
    axes[2, 2].set_ylabel("mol*s$^{-1}$, $10^{-20}$", fontname="Arial", fontsize=24)
    axes[2, 2].set_xlabel("Time, s", fontname="Arial", fontsize=24)

    return fig
    # plt.show()
    #
    # # plt.savefig(os.path.join('SM5f ASOR+TPC+ClC+H-leak low Cl.svg'), transparent=True)
